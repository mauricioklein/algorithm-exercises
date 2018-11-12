require 'spec_helper'

RSpec.describe Solver do
  subject { described_class.new.call(people) }

  describe "Test case #1" do
    let(:people) do
      [
        [1, 10],
        [3,  7]
      ]
    end

    let(:expected_result) { 3 }

    it { is_expected.to eq(expected_result) }
  end

  describe "Test case #2" do
    let(:people) do
      [
        [1950, 2010],
        [1960, 1990],
        [1955, 2011]
      ]
    end

    let(:expected_result) { 1960 }

    it { is_expected.to eq(expected_result) }
  end

  describe "Test case #3" do
    let(:people) do
      [
        [1950, 1970],
        [1980, 2000],
        [1965, 1985]
      ]
    end

    let(:expected_result) { 1965 }

    it { is_expected.to eq(expected_result) }
  end
end
