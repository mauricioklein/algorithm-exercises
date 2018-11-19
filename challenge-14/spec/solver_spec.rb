require 'spec_helper'

RSpec.describe Solver do
  subject { described_class.new.call(dict, word) }

  let(:dict) do
    %w(tea ted ten inn)
  end

  describe "with exact match" do
    let(:word) { "tea" }

    it { is_expected.to contain_exactly("tea") }
  end

  describe "with words matching prefix" do
    let(:word) { "te" }

    it { is_expected.to contain_exactly("tea", "ted", "ten") }
  end

  describe "with no word matching prefix" do
    let(:word) { "ba" }

    it { is_expected.to be_empty }
  end

  describe "with empty string" do
    let(:word) { "" }

    it { is_expected.to be_empty }
  end
end
