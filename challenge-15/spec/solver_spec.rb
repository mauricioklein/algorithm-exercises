require 'spec_helper'

RSpec.describe Solver do
  subject { described_class.new.call(steps) }

  describe "with 1 step" do
    let(:steps) { 1 }

    it { is_expected.to eq(1) }
  end

  describe "with 2 steps" do
    let(:steps) { 2 }

    it { is_expected.to eq(2) }
  end

  describe "with 4 steps" do
    let(:steps) { 4 }

    it { is_expected.to eq(5) }
  end

  describe "with 100 steps" do
    let(:steps) { 100 }

    it { is_expected.to eq(573147844013817084101) }
  end
end
